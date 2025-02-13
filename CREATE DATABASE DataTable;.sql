CREATE DATABASE DataTable;

CREATE TABLE dataTable (
    object_id INT PRIMARY KEY,
    domain VARCHAR(50),
    kingdom VARCHAR(50),
    phylum VARCHAR(50),
    class VARCHAR(50),
    order VARCHAR(50),
    family VARCHAR(50),
    genus VARCHAR(50),
    species VARCHAR(50)
);

INSERT INTO dataTable (object_id, domain, kingdom, phylum, class, order, family, genus, species)
VALUES
    (1, "Eukarya", "Animalia", "Arthropoda", "Hexapoda", "Insecta", "Diptera", "Drosophilidae", "Drosophila", "D. melanogaster");

SELECT * FROM employees;