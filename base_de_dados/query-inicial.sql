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

INSERT INTO Livros(Titulo, Genero, Tema, NumeroDePaginas, AnoDeLancamento, GeneroProtagonista, IdiomaOriginal, 
                   ComplexidadeDaLinguagem, Populariedade, PublicoAlvo, Narrador)
VALUES
-- 1
("A Menina que Roubava Livros", "Drama", "Segunda Guerra Mundial", 480, 2005, "F", "Alemão", "Moderada", "Muito Popular", "Jovem Adulto", "Narrador Onisciente"),

-- 2
("1984", "Ficção Científica", "Distopia Totalitária", 328, 1949, "M", "Inglês", "Complexa", "Muito Popular", "Adulto", "3 pessoa"),

-- 3
("Extraordinário", "Drama", "Superação", 320, 2012, "M", "Inglês", "Simples", "Popular", "Jovem Adulto", "1 pessoa"),

-- 4
("O Pequeno Príncipe", "Fábula", "Amizade e Amor", 96, 1943, "M", "Francês", "Simples", "Muito Popular", "Infantil", "1 pessoa"),

-- 5
("Jogos Vorazes", "Ação", "Revolução", 374, 2008, "F", "Inglês", "Moderada", "Muito Popular", "Jovem Adulto", "1 pessoa"),

-- 6
("Orgulho e Preconceito", "Romance", "Relacionamentos", 432, 1813, "F", "Inglês", "Complexa", "Muito Popular", "Adulto", "3 pessoa"),

-- 7
("A Revolução dos Bichos", "Fábula Política", "Ditadura", 152, 1945, "M", "Inglês", "Simples", "Popular", "Adulto", "Narrador Onisciente"),

-- 8
("Coraline", "Terror", "Mundo Paralelo", 208, 2002, "F", "Inglês", "Moderada", "Popular", "Jovem Adulto", "3 pessoa"),

-- 9
("O Hobbit", "Fantasia", "Jornada", 310, 1937, "M", "Inglês", "Moderada", "Muito Popular", "Jovem Adulto", "Narrador Onisciente"),

-- 10
("Dom Casmurro", "Romance", "Ciúmes", 256, 1899, "M", "Português", "Complexa", "Popular", "Adulto", "1 pessoa"),

-- 11
("A Seleção", "Romance", "Sociedade Distópica", 368, 2012, "F", "Inglês", "Simples", "Muito Popular", "Jovem Adulto", "1 pessoa"),

-- 12
("Cidade dos Ossos", "Fantasia Urbana", "Luta entre Sombras", 512, 2007, "F", "Inglês", "Moderada", "Popular", "Jovem Adulto", "1 pessoa"),

-- 13
("Ensaio sobre a Cegueira", "Drama", "Colapso Social", 320, 1995, "M", "Português", "Complexa", "Popular", "Adulto", "Narrador Onisciente"),

-- 14
("O Diário de Anne Frank", "Biografia", "Holocausto", 384, 1947, "F", "Holandês", "Simples", "Muito Popular", "Jovem Adulto", "1 pessoa"),

-- 15
("It: A Coisa", "Terror", "Infância e Medo", 1104, 1986, "M", "Inglês", "Complexa", "Muito Popular", "Adulto", "Narrador Onisciente");


ALTER TABLE Livros CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
