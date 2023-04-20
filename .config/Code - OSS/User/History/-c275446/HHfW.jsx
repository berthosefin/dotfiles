export default function Fruit(props){
    //state

    //comportements

    //render
    return <div>
        <li key={props.fruit.id}>
            {props.fruit.nom}
            <button onClick={() => props.onFruitDelete(props.fruit.id)}>x</button>
        </li>
    </div>
}