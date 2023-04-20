import { Todo } from "@/typings";
import Link from "next/link";

const fetchTodos = async () => {
  const res = await fetch("http://127.0.0.1:3001/todos");
  const todos: Todo = await res.json();
  return todos;
};

export default async function TodosList() {
  const todos = await fetchTodos();

  return (
    <>
      {/* @ts-ignore */}
      {todos.map((todo) => (
        <p key={todo.id}>
          <Link href={`/todos/${todo.id}`}>Todo: {todo.id}</Link>
        </p>
      ))}
    </>
  );
}
