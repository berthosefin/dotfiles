export default function FruitForm(){
    // state
    // const fruitInfo = props.fruitInfo
    // const onFruitDelete = props.onFruitDelet


    // comportements

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