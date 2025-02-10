import reflex as rx

from ..backend.backend import State,EmployeeDeductionEntry  # Asumsi State menyediakan method load_entries, add_employee_entry, dll.
from ..components.form_field import form_field
from ..components.status_badges import status_badge

class Table(rx.State):
    color_map: dict[str,str]={
        "transfer": "blue",
        "cash":"cyan",
    }
    

def show_employee_deduction(entry: EmployeeDeductionEntry) -> rx.Component:
    print("Rendering entry:", entry.__dict__)
    """Tampilkan satu baris data employee_deduction dalam tabel."""
    return rx.table.row(
        rx.table.cell(entry.name),
        rx.table.cell(entry.nip),
        rx.table.cell(entry.arisan),
        rx.table.cell(entry.denda_arisan),
        rx.table.cell(entry.iuran_dw),
        rx.table.cell(entry.simpanan_wajib_koperasi),
        rx.table.cell(entry.belanja_koperasi),
        rx.table.cell(entry.simpanan_pokok),
        rx.table.cell(entry.kredit_khusus),
        rx.table.cell(entry.kredit_barang),
        rx.table.cell(entry.date),
        rx.table.cell(
            rx.match(
                entry.status,
                ("paid", status_badge("paid")),  # Tambahkan warna
                ("unpaid", status_badge("unpaid")),  # Tambahkan warna
                ("installment", status_badge("installment")),  # Tambahkan warna
                status_badge("unpaid"),  # Default jika tidak match
            )
        ),
        rx.table.cell(rx.badge(
            entry.payment_type,
            color_scheme=Table.color_map[entry.payment_type],
            size="3",
            ),
        ),
        rx.table.cell(
            rx.hstack(
                # Download button
                rx.icon_button(
                    rx.icon("download", size=22),
                    on_click=lambda: State.download_deduction_slip(entry),
                    size="2",
                    variant="solid",
                    color_scheme="grass",
                ),
                # Edit button
                update_employee_dialog(entry),
                confirm_delete_dialog(entry),
                spacing="2",
            )
        ),
        style={"_hover": {"bg": rx.color("gray", 3)}},
        align="center",
    )


def add_employee_button() -> rx.Component:
    """Dialog untuk menambah data employee_deduction baru."""
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add Entry", size="4", display=["none", "none", "block"]),
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="clipboard", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title("Add New Entry", weight="bold", margin="0"),
                    rx.dialog.description("Fill the form with the employee deduction info"),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        # Nama & NIP
                        form_field("Nama", "Employee Name", "text", "name", "user"),
                        form_field("NIP", "Employee NIP", "text", "nip", "id-card"),
                        # Deduction amounts
                        form_field("Arisan", "Amount for Arisan", "number", "arisan", "dollar-sign"),
                        form_field("Denda Arisan", "Amount for Denda Arisan", "number", "denda_arisan", "dollar-sign"),
                        form_field("Iuran DW", "Amount for Iuran DW", "number", "iuran_dw", "dollar-sign"),
                        form_field("Simpanan Wajib Koperasi", "Amount for Simpanan Wajib Koperasi", "number", "simpanan_wajib_koperasi", "dollar-sign"),
                        form_field("Belanja Koperasi", "Amount for Belanja Koperasi", "number", "belanja_koperasi", "dollar-sign"),
                        form_field("Simpanan Pokok", "Amount for Simpanan Pokok", "number", "simpanan_pokok", "dollar-sign"),
                        form_field("Kredit Khusus", "Amount for Kredit Khusus", "number", "kredit_khusus", "dollar-sign"),
                        form_field("Kredit Barang", "Amount for Kredit Barang", "number", "kredit_barang", "dollar-sign"),
                        # Payment Status
                        rx.vstack(
                            rx.hstack(
                                rx.icon("truck", size=16, stroke_width=1.5),
                                rx.text("Status"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["paid", "unpaid", "installment"],
                                name="status",
                                direction="row",
                                as_child=True,
                                required=True,
                            ),
                        ),
                        # Payment Type
                        rx.vstack(
                            rx.hstack(
                                rx.icon("credit-card", size=16, stroke_width=1.5),
                                rx.text("Type"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["cash", "transfer"],
                                name="payment_type",
                                direction="row",
                                as_child=True,
                                required=True,
                            ),
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button("Cancel", variant="soft", color_scheme="gray"),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Submit Entry"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=State.add_employee_entry,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )
def update_employee_dialog(entry) -> rx.Component:
    """Dialog untuk mengedit data employee_deduction yang sudah ada."""
    print("Entry status:", entry.status)  # Debug print
    print("Entry payment_type:", entry.payment_type)
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("square-pen", size=22),
                color_scheme="blue",
                size="2",
                variant="solid",
                on_click=lambda: State.get_entry(entry),
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="square-pen", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title("Edit Entry", weight="bold", margin="0"),
                    rx.dialog.description("Edit the employee deduction info"),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        form_field(
                            "Nama", 
                            "Employee Name", 
                            "text", 
                            "name", 
                            "user", 
                            entry.name,
                        ),
                        form_field(
                            "NIP", 
                            "Employee NIP", 
                            "text", 
                            "nip", 
                            "id-card", 
                            entry.nip,
                        ),
                        form_field(
                            "Arisan", 
                            "Amount for Arisan", 
                            "number", 
                            "arisan", 
                            "dollar-sign", 
                            entry.arisan.to(str),
                        ),
                        form_field(
                            "Denda Arisan", 
                            "Amount for Denda Arisan", 
                            "number", 
                            "denda_arisan", 
                            "dollar-sign", 
                            entry.denda_arisan.to(str),
                        ),
                        form_field(
                            "Iuran DW", 
                            "Amount for Iuran DW", 
                            "number", 
                            "iuran_dw", 
                            "dollar-sign", 
                            entry.iuran_dw.to(str),
                        ),
                        form_field(
                            "Simpanan Wajib Koperasi", 
                            "Amount for Simpanan Wajib Koperasi", 
                            "number", 
                            "simpanan_wajib_koperasi", 
                            "dollar-sign", 
                            entry.simpanan_wajib_koperasi.to(str),
                        ),
                        form_field(
                            "Belanja Koperasi", 
                            "Amount for Belanja Koperasi", 
                            "number", 
                            "belanja_koperasi", 
                            "dollar-sign", 
                            entry.belanja_koperasi.to(str),
                        ),
                        form_field(
                            "Simpanan Pokok", 
                            "Amount for Simpanan Pokok", 
                            "number", 
                            "simpanan_pokok", 
                            "dollar-sign", 
                            entry.simpanan_pokok.to(str),
                        ),
                        form_field(
                            "Kredit Khusus", 
                            "Amount for Kredit Khusus", 
                            "number", 
                            "kredit_khusus", 
                            "dollar-sign", 
                            entry.kredit_khusus.to(str),
                        ),
                        form_field(
                            "Kredit Barang", 
                            "Amount for Kredit Barang", 
                            "number", 
                            "kredit_barang", 
                            "dollar-sign", 
                            entry.kredit_barang.to(str),
                        ),
                        # Status
                        rx.vstack(
                            rx.hstack(
                                rx.icon("truck", size=16, stroke_width=1.5),
                                rx.text("Status"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["paid", "unpaid", "installment"],
                                default_value=entry.status,
                                name="status",
                                direction="row",
                                as_child=True,
                                required=True,     
                            ),
                        ),
                        # Radio button untuk Payment Type dengan default_value
                        rx.vstack(
                            rx.hstack(
                                rx.icon("credit-card", size=16, stroke_width=1.5),
                                rx.text("Type"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["cash", "transfer"],
                                default_value=entry.payment_type,
                                name="payment_type",
                                direction="row",
                                as_child=True,
                                required=True,
                            ),
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button("Cancel", variant="soft", color_scheme="gray"),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Update Entry"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=State.update_employee_entry,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )
    
def confirm_delete_dialog(entry) -> rx.Component:
    """Displays a confirmation dialog before deleting an entry."""
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.icon_button(
                rx.icon("trash-2", size=22),
                size="2",
                variant="solid",
                color_scheme="red",
            )
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title("Delete Users"),
            rx.alert_dialog.description(
                "Are you sure you want to delete this user? This action is permanent and cannot be undone.",
                size="2",
            ),
            rx.inset(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("Full Name"),
                            rx.table.column_header_cell("NIP"),
                        ),
                    ),
                    rx.table.body(
                        rx.table.row(
                            rx.table.cell(entry.name),
                            rx.table.cell(entry.nip),
                        ),
                    ),
                ),
                side="x",
                margin_top="24px",
                margin_bottom="24px",
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button("Cancel", variant="soft", color_scheme="gray"),
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Delete user",
                        color_scheme="red",
                        on_click=lambda: State.delete_employee(entry.id), # Panggil fungsi backend
                    ),
                ),
                spacing="3",
                justify="end",
            ),
            style={"max_width": 500},
        ),
    )





def _header_cell(text: str, icon: str) -> rx.Component:
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )

def _pagination_view() -> rx.Component:
    """Tampilan kontrol pagination."""
    return rx.hstack(
        rx.text(
            "Page ",
            rx.code(State.page_number),
            f" of {State.total_pages}",
            justify="end",
        ),
        rx.hstack(
            rx.icon_button(
                rx.icon("chevrons-left", size=18),
                on_click=State.first_page,
                opacity=rx.cond(State.page_number == 1, 0.6, 1),
                color_scheme=rx.cond(State.page_number == 1, "gray", "accent"),
                variant="soft",
            ),
            rx.icon_button(
                rx.icon("chevron-left", size=18),
                on_click=State.prev_page,
                opacity=rx.cond(State.page_number == 1, 0.6, 1),
                color_scheme=rx.cond(State.page_number == 1, "gray", "accent"),
                variant="soft",
            ),
            rx.icon_button(
                rx.icon("chevron-right", size=18),
                on_click=State.next_page,
                opacity=rx.cond(State.page_number == State.total_pages, 0.6, 1),
                color_scheme=rx.cond(State.page_number == State.total_pages, "gray", "accent"),
                variant="soft",
            ),
            rx.icon_button(
                rx.icon("chevrons-right", size=18),
                on_click=State.last_page,
                opacity=rx.cond(State.page_number == State.total_pages, 0.6, 1),
                color_scheme=rx.cond(State.page_number == State.total_pages, "gray", "accent"),
                variant="soft",
            ),
            align="center",
            spacing="2",
            justify="end",
        ),
        spacing="5",
        margin_top="1em",
        align="center",
        width="100%",
        justify="end",
    )


def month_navigation() -> rx.Component:
    """Komponen navigasi bulan."""
    return rx.hstack(
        rx.icon_button(
            rx.icon("chevron-left"),
            on_click=State.prev_month,
            variant="ghost",
        ),
        rx.badge(
            rx.center(
                State.formatted_month,
                width="100%",
            ),
            variant="surface",
            min_width="150px",
            text_align="center",
            size="3",
        ),
        rx.icon_button(
            rx.icon("chevron-right"),
            on_click=State.next_month,
            variant="ghost",
        ),
        spacing="3",
    )
    
def main_table() -> rx.Component:
    return rx.fragment(
        rx.flex(
            add_employee_button(),
            rx.spacer(),
            month_navigation(),  # Tambahkan navigasi bulan
            rx.cond(
                State.sort_reverse,
                rx.icon(
                    "arrow-down-z-a",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
                rx.icon(
                    "arrow-down-a-z",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
            ),
            rx.select(
                ["name", "nip", "date", "status"],
                placeholder="Sort By: Name",
                size="3",
                on_change=lambda sort_value: State.sort_values(sort_value),
            ),
            rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Search here...",
                size="3",
                max_width="225px",
                width="100%",
                variant="surface",
                on_change=lambda value: State.filter_values(value),
            ),
            justify="end",
            align="center",
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Nama", "user"),
                    _header_cell("NIP", "id-card"),
                    _header_cell("Arisan", "dollar-sign"),
                    _header_cell("Denda Arisan", "dollar-sign"),
                    _header_cell("Iuran DW", "dollar-sign"),
                    _header_cell("Simpanan Wajib Koperasi", "dollar-sign"),
                    _header_cell("Belanja Koperasi", "dollar-sign"),
                    _header_cell("Simpanan Pokok", "dollar-sign"),
                    _header_cell("Kredit Khusus", "dollar-sign"),
                    _header_cell("Kredit Barang", "dollar-sign"),
                    _header_cell("Date", "calendar"),
                    _header_cell("Status", "truck"),
                    _header_cell("Type", "tag"),
                    _header_cell("Actions", "cog"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    State.current_page_entries,
                    lambda x: show_employee_deduction(x)
                )
            ),
            variant="surface",
            size="3",
            width="100%",
            on_mount=State.load_entries,
        ),
        _pagination_view(),
    )