export default function Fruit(props){
    //state
    const fruitInfo = props.fruitInfo
    const onFruitDelete = props.onFruitDelete

    //comportements

    //render
    return <div>
        <li key={props.fruitInfo.id}>
            {props.fruitInfo.nom}
            <button onClick={() => props.onFruitDelete(props.fruitInfo.id)}>x</button>
        </li>
    </div>
}