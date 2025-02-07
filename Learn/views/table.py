import reflex as rx

from ..backend.backend import State  # Asumsi State menyediakan method load_entries, add_employee_entry, dll.
from ..components.form_field import form_field
from ..components.status_badges import status_badge


def show_employee_deduction(entry) -> rx.Component:
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
                ("paid", status_badge("Paid")),
                ("unpaid", status_badge("Unpaid")),
                ("installment", status_badge("Installment")),
                status_badge("Unpaid"),
            )
        ),
        rx.table.cell(entry.payment_type),
        rx.table.cell(
            rx.hstack(
                update_employee_dialog(entry),
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: State.delete_employee(entry.id),
                    size="2",
                    variant="solid",
                    color_scheme="red",
                ),
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
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("square-pen", size=22),
                rx.text("Edit", size="3"),
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
                        form_field("Nama", "Employee Name", "text", "name", "user", entry.name),
                        form_field("NIP", "Employee NIP", "text", "nip", "id-card", entry.nip),
                        form_field("Arisan", "Amount for Arisan", "number", "arisan", "dollar-sign", entry.arisan),
                        form_field("Denda Arisan", "Amount for Denda Arisan", "number", "denda_arisan", "dollar-sign", entry.denda_arisan),
                        form_field("Iuran DW", "Amount for Iuran DW", "number", "iuran_dw", "dollar-sign", entry.iuran_dw),
                        form_field("Simpanan Wajib Koperasi", "Amount for Simpanan Wajib Koperasi", "number", "simpanan_wajib_koperasi", "dollar-sign", entry.simpanan_wajib_koperasi),
                        form_field("Belanja Koperasi", "Amount for Belanja Koperasi", "number", "belanja_koperasi", "dollar-sign", entry.belanja_koperasi),
                        form_field("Simpanan Pokok", "Amount for Simpanan Pokok", "number", "simpanan_pokok", "dollar-sign", entry.simpanan_pokok),
                        form_field("Kredit Khusus", "Amount for Kredit Khusus", "number", "kredit_khusus", "dollar-sign", entry.kredit_khusus),
                        form_field("Kredit Barang", "Amount for Kredit Barang", "number", "kredit_barang", "dollar-sign", entry.kredit_barang),
                        rx.vstack(
                            rx.hstack(
                                rx.icon("truck", size=16, stroke_width=1.5),
                                rx.text("Status"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["paid", "unpaid", "installment"],
                                default_value=entry.status ,
                                name="status",
                                direction="row",
                                as_child=True,
                                required=True,
                            ),
                        ),
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


def _header_cell(text: str, icon: str) -> rx.Component:
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def main_table() -> rx.Component:
    return rx.fragment(
        rx.flex(
            add_employee_button(),
            rx.spacer(),
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
            rx.table.body(rx.foreach(State.entries, show_employee_deduction)),
            variant="surface",
            size="3",
            width="100%",
            on_mount=State.load_entries,
        ),
    )