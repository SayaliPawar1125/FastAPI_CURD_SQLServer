CREATE DATABASE MasterCategoryDB;

USE MasterCategoryDB;

CREATE TABLE MasterCategory
(
    MasterCategoryId INT IDENTITY(1,1) PRIMARY KEY,
    MasterCategoryName VARCHAR(100) NOT NULL
);

INSERT INTO MasterCategory (MasterCategoryName)
VALUES
('Java'),
('Python'),
('React'),
('SQL');