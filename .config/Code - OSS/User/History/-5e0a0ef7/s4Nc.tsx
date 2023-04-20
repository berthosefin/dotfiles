type FormData = {
  id: string;
  title: string;
  content: string;
};

type Props = {
  formData: FormData;
  setFormData: () => {};
};

export default function AddNoteForm({ formData, setFormData }: Props) {
  return (
    <div>
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
          onChange={(e) => setForm({ ...form, title: e.target.value })}
          className="border-2 rounded border-gray-600 p-1"
        />
        <textarea
          placeholder="Content"
          value={form.content}
          onChange={(e) => setForm({ ...form, content: e.target.value })}
          className="border-2 rounded border-gray-600 p-1"
        />
        <button type="submit" className="bg-blue-500 text-white rounded p-1">
          Add +
        </button>
      </form>
    </div>
  );
}
