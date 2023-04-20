import { setFlagsFromString } from "v8";

export default function Home() {
  return (
    <div>
      <h1 className="text-center font-bold text-2xl mt-4">Notes</h1>
      <form
        onSubmit={(e) => {
          e.preventDefault();
        }}
        className="w-auto min-w-[25%] max-w-min mx-auto space-y-6 flex flex-col items-stretch"
      >
        <input
          type="text"
          placeholder="Title"
          value={form.title}
          onChange={(e) =>
            setFlagsFromString({ ...form, title: e.target.value })
          }
          className="border-2 rounded border-gray-600 p-1"
        />
        <textarea
          placeholder="Content"
          value={form.content}
          onChange={(e) =>
            setFlagsFromString({ ...form, content: e.target.value })
          }
          className="border-2 rounded border-gray-600 p-1"
        />
      </form>
    </div>
  );
}
