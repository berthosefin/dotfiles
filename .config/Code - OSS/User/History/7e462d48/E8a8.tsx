export default function Home() {
  return (
    <div>
      <h1 className="text-center font-bold text-2xl mt-4">Notes</h1>
      <form
        onSubmit={(e) => {
          e.preventDefault();
        }}
      ></form>
    </div>
  );
}
