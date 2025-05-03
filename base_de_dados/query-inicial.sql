use db;

CREATE TABLE students(
    StudentID int not null AUTO_INCREMENT,
    FirstName varchar(100) NOT NULL,
    Surname varchar(100) NOT NULL,
    PRIMARY KEY (StudentID)
);

CREATE TABLE Livros(
    LivroID int not null AUTO_INCREMENT,
    Titulo varchar(255) NOT NULL,
    Genero varchar(255) NOT NULL,
    Tema varchar(255) NOT NULL,
    NumeroDePaginas int NOT NULL,
    AnoDeLancamento int NOT NULL,
    GeneroProtagonista varchar(100) NOT NULL,
    IdiomaOriginal varchar(100) NOT NULL,
    ComplexidadeDaLinguagem varchar(100) NOT NULL,
    Populariedade varchar(100) NOT NULL,
    PublicoAlvo varchar(100) NOT NULL,
    Narrador varchar(100) NOT NULL,
    PRIMARY KEY (LivroID )
);



INSERT INTO students(FirstName, Surname)
VALUES("John", "Andersen"), ("Emma", "Smith");  