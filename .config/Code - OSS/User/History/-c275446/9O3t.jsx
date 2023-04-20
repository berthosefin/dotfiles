export default function Fruit(props){
    //state

    //comportements

    //render
    return <div>
        <li key={props.fruit.id}>
            {props.fruit.nom}
            <button onClick={() => handleDelete(props.fruit.id)}>x</button>
        </li>
    </div>
}