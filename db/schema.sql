-- Protein/Carbs/Fat/Fiber measured in grams.
CREATE TABLE Ingredient (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL UNIQUE,
    CaloriesPerGram REAL NOT NULL,
    ProteinPerGram REAL NOT NULL,
    CarbsPerGram REAL NOT NULL,
    FatPerGram REAL NOT NULL,
    FiberPerGram REAL NOT NULL,

    BaseUnit TEXT NOT NULL CHECK(
        BaseUnit IN ('g','kg','oz','lb','floz','mL','L','cup','tsp','tbsp')),

    -- Grams per BaseUnit, to be used to later populate QuantityInGrams (RecipeIngredient)
    GramConversion REAL NOT NULL                
);

-- Recipe steps will be delimited with a special character
-- so that they can later be treated like a list.
CREATE TABLE Recipe (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL UNIQUE,
    Steps TEXT NOT NULL,
    BaseServings INTEGER NOT NULL,
    Description TEXT NOT NULL,
    Notes TEXT
);

/*
- Unit stores original recipe unit to preserve readability
- Quantity refers to original 'base' Unit
- QuantityInGrams converts (with an appropriate ratio) the base unit to grams to facilitate nutrition calculations
*/
CREATE TABLE RecipeIngredient (
    RecipeID INTEGER NOT NULL,
    IngredientId INTEGER NOT NULL,

    Quantity REAL NOT NULL,
    Unit TEXT NOT NULL,

    QuantityInGrams REAL NOT NULL,

    PRIMARY KEY (RecipeId, IngredientId),
    FOREIGN KEY (RecipeId) REFERENCES Recipe(Id),
    FOREIGN KEY (IngredientId) REFERENCES Ingredient(Id)
);