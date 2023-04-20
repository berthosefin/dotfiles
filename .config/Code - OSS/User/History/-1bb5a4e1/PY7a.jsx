import { useState } from "react";

export default function FruitForm(){
    // state
    const [nouveauFruit, setNouveauFruit] = useState("")


    // comportements
    const handleSubmit = (event) => {
        event.preventDefault();
        //1. copie du state
        const fruitsCopy = [...fruits]
    
        //2. manipulation de la copie du state
        const id = new Date().getTime()
        const nom = nouveauFruit
        const fruitAAjouter = {id, nom}
        fruitsCopy.push(fruitAAjouter)
    
        //3. modification du state avec le setter
        setFruits(fruitsCopy)
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