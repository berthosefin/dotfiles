import { useState } from "react";

function App() {
  // état (state, data)
  const [fruits, setFruits] = useState([
    {id: 1, nom: "Abricot"},
    {id: 2, nom: "Banane"},
    {id: 3, nom: "Cerise"},
  ]);

  // comportements

  // affichage (render)
  return (
    <div>
      <h1>Liste de fruits</h1>
      <ul>{}</ul>
    </div>
  )
}

export default App;
