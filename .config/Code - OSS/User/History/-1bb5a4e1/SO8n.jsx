import { useState } from "react";

export default function FruitForm({handleAdd}){
    // state
    const [nouveauFruit, setNouveauFruit] = useState("")

    // comportements
    const handleSubmit = (event) => {
        event.preventDefault();
        const id = new Date().getTime()
        const nom = nouveauFruit
        const fruitAAjouter = {id, nom}

        setNouveauFruit("")
      };
    
      const handleChange = (event) => {
        setNouveauFruit(event.target.value)
      }

    // render
    return (
        <form action="submit" onSubmit={handleSubmit}>
            <input 
                type="text"
                placeholder="Ajouter un fruit..." 
                value={nouveauFruit} 
                onChange={handleChange} />
            <button>Ajouter +</button>
        </form>
    )
}