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
  return <div>AddNoteForm</div>;
}
