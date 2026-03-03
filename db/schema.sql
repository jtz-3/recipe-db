CREATE TABLE Ingredient (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL UNIQUE,
    CaloriesPerGram REAL NOT NULL,
    ProteinPerGram REAL NOT NULL,
    CarbsPerGram REAL NOT NULL,
    FatPerGram REAL NOT NULL,
    FiberPerGram REAL NOT NULL
);

CREATE TABLE Recipe (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL UNIQUE,
    BaseServings INTEGER NOT NULL
);

CREATE TABLE RecipeIngredient (
    RecipeID INTEGER NOT NULL,
    IngredientId INTEGER NOT NULL,
    QuantityInGrams REAL NOT NULL,

    PRIMARY KEY (RecipeId, IngredientId),
    FOREIGN KEY (RecipeId) REFERENCES Recipe(Id),
    FOREIGN KEY (IngredientId) REFERENCES Ingredient(Id)
);