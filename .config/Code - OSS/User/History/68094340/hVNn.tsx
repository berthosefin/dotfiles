import { Todo } from "@/typings";

const fetchTodos = async () => {
  const res = await fetch("http://127.0.0.1:3001/todos");
  const todos: Todo = await res.json();
  return todos;
};

export default async function TodosList() {
  const todos = await fetchTodos();

  return <div>TodosList</div>;
}
