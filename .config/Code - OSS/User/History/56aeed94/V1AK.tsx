export default function Home() {
  return (
    <main className="p-4">
      <h1 className="text-slate-100 text-center text-xl">AGENDA</h1>
      <div className="grid grid-cols-1 place-items-center">
        <form className="bg-gray-800 p-4 w-[80vw] md:w-[40vw]">
          <div className="flex flex-col gap-4">
            <label className="text-slate-100 ">Title</label>
            <input
              className="form-input border-none rounded-md invert-[1]"
              type="text"
              name="title"
              placeholder="Title"
            />
          </div>
          <div className="flex flex-col gap-4">
            <label className="text-slate-100 ">Title</label>
            <input
              className="form-input border-none rounded-md invert-[1]"
              type="text"
              name="title"
              placeholder="Title"
            />
          </div>
          <div className="flex flex-col gap-4">
            <label className="text-slate-100 ">Title</label>
            <input
              className="form-input border-none rounded-md invert-[1]"
              type="text"
              name="title"
              placeholder="Title"
            />
          </div>
        </form>
      </div>
    </main>
  );
}
