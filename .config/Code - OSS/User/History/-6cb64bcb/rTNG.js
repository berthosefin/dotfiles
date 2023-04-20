import { useState } from "react";
import FruitForm from "./components/FruitForm";
import Fruit from "./components/Fruits";

function App() {
  // state
  const [fruits, setFruits] = useState([
    {id: 1, nom: "Abricot"},
    {id: 2, nom: "Banane"},
    {id: 3, nom: "Cerise"},
  ]);

  // comportements
  const handleDelete = (id) => {
    //1. copie du state
    const fruitsCopy = [...fruits];

    //2. manipuler la copie du state
    const fruitsCopyUpdated = fruitsCopy.filter(fruit => fruit.id !== id);

    //3. modifier le state avec le setter
    setFruits(fruitsCopyUpdated);
  };

  const handleAdd = (fruitAAjouter) => {
    //1. copie du state
    const fruitsCopy = [...fruits]

    //2. manipulation de la copie du state
    fruitsCopy.push(fruitAAjouter)

    //3. modification du state avec le setter
    setFruits(fruitsCopy)
  }

  // render
  return (
    <div>
      <h1>Liste de fruits</h1>
      <ul>
        {fruits.map((fruit) => (
          <Fruit fruitInfo={fruit} onFruitDelete={handleDelete}/>
        ))}
      </ul>
      <FruitForm handleAdd={handleAdd} />
    </div>
  )
}

export default App;

// Gestion du formulaire
//1. Création du formulaire
//2. Soumission du formulaire
//3. Collecte des données du formulaire
