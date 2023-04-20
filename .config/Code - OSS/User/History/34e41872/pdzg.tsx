import { Todo } from "@/typings";

type PageProps = {
  params: {
    todoId: string;
  };
};

const fetchTodo = async (todoId: string) => {
  const res = await fetch(`http://127.0.0.1:3001/todos/${todoId}`, {
    next: { revalidate: 60 },
  });
  const todo: Todo = await res.json();
  return todo;
};

export default async function TodoPage({ params: { todoId } }: PageProps) {
  const todo = await fetchTodo(todoId);
  return (
    <div className="p-10 bg-yellow-200 border-2 m-2 shadow-lg">
      <p>
        #{todo.id}: {todo.title}
      </p>
      <p>Completed: {todo.completed ? "Yes" : "No"} </p>
      <p className="border-t border-black mt-5 text-right">
        By User: {todo.userId}
      </p>
    </div>
  );
}

export async function generateStaticParams() {
  const res = await fetch("http://127.0.0.1:3001/todos");
  const todos: Todo = await res.json();
}
