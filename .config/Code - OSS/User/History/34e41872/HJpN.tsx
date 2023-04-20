type PageProps = {
  params: {
    todoId: string;
  };
};

export default function TodoPage({ params: { todoId } }: PageProps) {
  return <div>TodoPage</div>;
}
