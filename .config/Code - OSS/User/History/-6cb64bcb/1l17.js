import { useState } from "react";

function App() {
  // état (state, data)
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
  }

  // affichage (render)
  return (
    <div>
      <h1>Liste de fruits</h1>
      <ul>
        {fruits.map((fruit) => (
          <li key={fruit.id}>
            {fruit.nom} <button onClick={() => handleDelete(fruit.id)}>x</button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App;
