-- SQLite
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    nip TEXT NOT NULL
);


-- Tabel Deductions
CREATE TABLE IF NOT EXISTS deductions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Tabel Employee_Deductions
CREATE TABLE IF NOT EXISTS employee_deductions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    deduction_id INTEGER NOT NULL,
    amount INTEGER,
    payment_status TEXT NOT NULL DEFAULT 'unpaid'
        CHECK (payment_status IN ('paid', 'unpaid', 'installment')),
    payment_type TEXT
        CHECK (payment_type IN ('cash', 'transfer') OR payment_type IS NULL),
    month INTEGER NOT NULL CHECK (month BETWEEN 1 AND 12),
    year INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE,
    FOREIGN KEY (deduction_id) REFERENCES deductions(id) ON DELETE CASCADE
);


-----------------------------------------------------------
-- 2. Memasukkan Data ke Tabel employees
-----------------------------------------------------------

INSERT INTO employees (name, nip) VALUES 
    ('Hermawan, SST', '198910142013111001'),
    ('Wd. Sri Marjanawati Oba, SE.Msi', '196701021992032001'),
    ('St. Rohima', '199506292022032015'),
    ('Emmanuella Caesarah', '199702052024212006'),
    ('Zuraida Rizki Rachmah, S.Tr.Stat.', '199510152019012001'),
    ('La Ode Haerul Saleh, SH', '198709052011011008'),
    ('Ardiman Adami', '198205112011011011'),
    ('Astutyningsih, SP', '198003112005022001'),
    ('Asrafiah', '198708102008012001'),
    ('St. Rasnani Manafi, SE. Msi.', '197603221998032001'),
    ('Diana Pratiwi Moningka', '198402092006042003'),
    ('Eka Baktiar', '198812052011011005'),
    ('Syamsiah R.', '196802171991012001'),
    ('Ramadan Salehani, SE', '198406022009111001'),
    ('Rezky Susanty Nurdin, A.Md', '198905292011012012'),
    ('Darul', '196912311992101001'),
    ('Slamet Riyadi, A.Md', '198606132009021004'),
    ('Komang Damike, A.Md', '198201052011011011'),
    ('Predi Siampa', '197012042006041010'),
    ('Yunus Samuel Tandibua', '197002052007011003'),
    ('Raimon MDS, SE', '197407051998031003'),
    ('Irma Suryani', '198510302012122002'),
    ('Wa Ode Hasmayuli, SST.', '199308222016022001'),
    ('Luluin Sabiqah S.Tr.Stat.', '199901162022012003'),
    ('La Riko, S.Ak.', '199403052022031009'),
    ('Fitharia Susiyanti, SE', '198309182011012010'),
    ('Muh. Mulyadi, SST', '198312152007011010'),
    ('Vianey Weda', '199007262013112001'),
    ('Muhamad Kadarsah, SP', '197410112006041002'),
    ('Farha Imamiah Gafar', '198404222005022002'),
    ('Fatimatuz Zahro, SST', '198601082009022004'),
    ('Wulan Isfah Jamil, SST', '198807062010122004'),
    ('Moh. Hardiansyah Mashar, SST', '199410232017011001'),
    ('Tri Halisir, SSi.', '199002122019031001'),
    ('Muhammad Haris La Ode, SST', '199102152014101001'),
    ('Denny Rizky Firmansyah, S.Tr.Stat.', '199612172019011001'),
    ('Ir. Surianti Toar, MS.', '196607161994012001'),
    ('Najmuddin Tamim, SST', '198708112010121004'),
    ('Parlindungan Siregar', '198805132010031001'),
    ('Maulida, SP.', '198101122005022002'),
    ('La Emi', '197312312003121012'),
    ('Zaima Nurrusydah, SST', '198812192010122004'),
    ('Irna Octaviana Latif', '198610262005022001'),
    ('Dini Amirul, S.ST, MIDS, M.Ec.Dev', '198712242009121001'),
    ('Syifa Reihana, SST', '199511172018022001'),
    ('Muh. Amin SE', '196707161993011001'),
    ('Mani Daud, SE. MS', '197210201994011001'),
    ('Wa Ode Rahmina Sari, SST', '198806222012112001'),
    ('Erra Septy Vibriane', '198309112009022007'),
    ('Sahunan Qola Jayati, S,ST', '198109162004122001'),
    ('Nurlyah, SST', '198701032009022004'),
    ('Fadhila Tsany Nur Rizky, SST', '199401312017012001'),
    ('Herawati', '198804102008012001'),
    ('Adiman Suriawan, SE. ME.', '198703152011011008'),
    ('Titin Yuniarty, SST', '198706192009122002'),
    ('Muh. Ahnan Prastito, SST', '199507192017011001'),
    ('Dyah Ayu Ratna N, SST.', '199009022014102001'),
    ('Mulawarman, SST', '198705112006041003'),
    ('Nike Roso Wulandari, SST', '198206182004122001'),
    ('Tino Aprilian', '199704102019121002'),
    ('Rachmatiah Rachman, SE.', '197501222001122001'),
    ('Fani Dewi Astuti, S.ST', '199110142014102001'),
    ('Rizkiani, SST', '198402122007012006'),
    ('Manggoa Joni', '197001271990021002'),
    ('Miftahtul Khair Anwar, SST', '198904302012112001'),
    ('Erni Octaviani, S.Tr.Stat.', '199710052019122001'),
    ('Amrin Barata, S.ST', '199006032014101001'),
    ('Burit Retnowati, S.ST', '197809242003122003'),
    ('Fatchur Rochman, SST.', '197907092000121002'),
    ('Harningsih, S. ST', '197906212000122002'),
    ('Agung Septianto Wibowo, SST', '198309282006021002'),
    ('Arizka Selviana, SST', '199001162013112001'),
    ('Damara Utama, S.Tr.Stat', '199604182019011002'),
    ('Khaidir', '198105212007101002'),
    ('Muhammad Rizal Karim, SST', '199505252018021002'),
    ('Evy Eriani', '197307032005022002'),
    ('Mochamad Wildan Maulana', '199904302022011003'),
    ('Muh. Arifiansyah Ayub, SST.', '199203162014121001'),
    ('Ridwan Kun Satria', '198009242011011006'),
    ('Wayan Permana Saputra, SST', '199303082014121001'),
    ('Suci Safitriani, SST', '199012162014102001'),
    ('Siti Rogayah, S.ST, M.S.E, M.P.P', '198708152009122005'),
    ('Sudirman', '196801012006041035'),
    ('Riyanti', '197505272014062001'),
    ('Hasyuril Hadini, SE', '196704201992121001'),
    ('Musdin, SST.', '197304161993121001'),
    ('Towedy ML', '197203221999031004'),
    ('Suharjufito Endo, SST', '198612152009021005'),
    ('Irfan Saputri', '198806142011012014'),
    ('Abd. Jalil', '7471021204900002'),
    ('Fitri', '7471085108840001'),
    ('Nur', '197506112002122003'),
    ('Putu Suweda', '7405191001910001'),
    ('Mat Asdi', '7471041202700001'),
    ('Ardin', '7471050206880002'),
    ('Arby', '7471020602910001'),
    ('Ifan Ansari', '7471091307800001'),
    ('Masdiana', '5371066709910001'),
    ('Muhammad Hafif Fudin', '7405030209020001');



-----------------------------------------------------------
-- 3. Memasukkan Data ke Tabel deductions
-----------------------------------------------------------

INSERT INTO deductions (name) VALUES
    ('Arisan'),
    ('Iuran DW'),
    ('Simpanan Wajib Koperasi'),
    ('Belanja Koperasi'),
    ('Simpanan Pokok'),
    ('Kredit Khusus'),
    ('Kredit Barang');


-- Hapus semua data dari tabel employee_deductions
DELETE FROM employee_deductions;

-- Hapus semua data dari tabel employees
DELETE FROM employees;

-- Hapus table employees
DROP TABLE employees;

-- Hapus table deductions
DROP TABLE deductions;

-- Hapus table employee_deductions
DROP TABLE employee_deductions;