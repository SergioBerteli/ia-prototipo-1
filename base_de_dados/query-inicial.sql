use db;

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

INSERT INTO Livros(Titulo, Genero, Tema, NumeroDePaginas, AnoDeLancamento, GeneroProtagonista, IdiomaOriginal, 
				   ComplexidadeDaLinguagem, Populariedade, PublicoAlvo, Narrador)
Values("O Ceifador", "Romance", "Ficção Distópica", 443, 2016, "M", "Inglês", "Simples", "Muito Popular", "Jovem Adulto", "Narrador Onisciente"),
("Doadores de sono", "Ficção Científica", "Ficção Distópica", 176, 2014, "F", "Inglês", "Simples", "Popular", "Jovem Adulto", "1 pessoa");

ALTER TABLE Livros CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
