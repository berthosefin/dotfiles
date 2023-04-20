import prisma from "@/prisma/client";
import Card from "@/components/Card";

type Agenda = {
  id: string;
  title: string;
  date: string;
  time_start: string;
  time_end: string;
  place: string;
};

const getAgendaList = async () => {
  const data = await prisma.Agenda.findMany({
    select: {
      id: true,
      title: true,
      date: true,
      time_start: true,
      time_end: true,
      place: true,
    },
  });
  return data;
};

export default async function AgendaList() {
  const agendaList = await getAgendaList();

  return (
    <div className="p-4 text-slate-100 space-y-4">
      <h1 className="text-xl">Agenda List</h1>
      <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Card agendList={agendaList} />
      </div>
    </div>
  );
}
