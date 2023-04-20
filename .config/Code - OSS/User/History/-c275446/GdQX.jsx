export default function Fruit(props){
    //state

    //comportements

    //render
    return <div>
        <li key={props.fruitInfo.id}>
            {props.fruitInfo.nom}
            <button onClick={() => props.onFruitDelete(props.fruitInfo.id)}>x</button>
        </li>
    </div>
}