import { useState } from "react";

function App() {
  // état (state, data)
  const [fruits, setFruits] = useState([
    {id: 1, nom: "Abricot"},
    {id: 2, nom: "Banane"},
    {id: 3, nom: "Cerise"},
  ]);

  // comportements
  const handleClick = () => {
    setCompteur(compteur + 1)
  }

  // affichage (render)
  return (
    <div>
      <h1>Liste de fruits</h1>
    </div>
  )
}

export default App;
