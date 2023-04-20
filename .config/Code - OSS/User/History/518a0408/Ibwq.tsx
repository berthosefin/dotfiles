import Link from "next/link";

type Agenda = {
  id: string;
  title: string;
  date: string;
};

export default function Card({ agendaList }: any) {
  return agendaList.map((agenda) => (
    <div key={agenda.id} className="bg-gray-800 p-4 relative">
      <button className="absolute top-2 right-4">x</button>
      <div className="space-y-2">
        <h1 className="text-2xl">{agenda.title}</h1>
        <p>{agenda.date}</p>
      </div>
      <div className="mt-4 text-right">
        <Link
          href={`/agenda-list/${agenda.id}`}
          className="bg-amber-600 rounded-md hover:bg-amber-700 hover:text-slate-20 px-6 py-2"
        >
          Detail
        </Link>
      </div>
    </div>
  ));
}
