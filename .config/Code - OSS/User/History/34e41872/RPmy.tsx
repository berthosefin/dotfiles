type PageProps = {
  params: {
    todoId: string;
  };
};

export default async function TodoPage({ params: { todoId } }: PageProps) {
  const todo = await fetchTodo(todoId);
  return <div>TodoPage: {todoId}</div>;
}
