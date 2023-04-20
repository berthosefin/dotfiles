export default function Home() {
  return (
    <main className="p-4">
      <h1 className="text-slate-100 text-center text-xl">AGENDA</h1>
      <div className="grid grid-cols-1 place-items-center">
        <form className="bg-gray-800 p-4 w-[80vw] md:w-[40vw]">
          <div>
            <label htmlFor=""></label>
            <input type="text" name="agenda" placeholder="Add detail" />
          </div>
        </form>
      </div>
    </main>
  );
}
