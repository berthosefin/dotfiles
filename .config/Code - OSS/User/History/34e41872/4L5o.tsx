type PageProps = {
  params: {
    todoId: string;
  };
};

const fetchTodo = async (todoId: string) => {
  const res = await fetch(`http://127.0.0.1:3000/todos/${todoId}`);
};

export default async function TodoPage({ params: { todoId } }: PageProps) {
  const todo = await fetchTodo(todoId);
  return <div>TodoPage: {todoId}</div>;
}
