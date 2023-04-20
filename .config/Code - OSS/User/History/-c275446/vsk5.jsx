export default function Fruit({fruitInfo, onFruitDelete}){
    // state
    // const fruitInfo = props.fruitInfo
    // const onFruitDelete = props.onFruitDelet


    // comportements

    // render
    return (
        <li>
            {fruitInfo.nom}{" "}
            <button onClick={() => onFruitDelete(fruitInfo.id)}>x</button>
        </li>
    )
}