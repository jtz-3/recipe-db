CREATE TABLE Ingredient (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL UNIQUE,
    CaloriesPerGram REAL NOT NULL,
    ProteinPerGram REAL NOT NULL,
    CarbsPerGram REAL NOT NULL,
    FatPerGram REAL NOT NULL,
    FiberPerGram REAL NOT NULL
);

-- Recipe steps will be delimited with a special character
-- so that they can later be treated like a list.
CREATE TABLE Recipe (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL UNIQUE,
    Steps TEXT NOT NULL,
    BaseServings INTEGER NOT NULL,
    Notes TEXT
);

CREATE TABLE RecipeIngredient (
    RecipeID INTEGER NOT NULL,
    IngredientId INTEGER NOT NULL,
    QuantityInGrams REAL NOT NULL,

    PRIMARY KEY (RecipeId, IngredientId),
    FOREIGN KEY (RecipeId) REFERENCES Recipe(Id),
    FOREIGN KEY (IngredientId) REFERENCES Ingredient(Id)
);