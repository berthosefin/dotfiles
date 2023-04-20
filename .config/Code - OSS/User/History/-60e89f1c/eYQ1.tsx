import prisma from "@/prisma/client";
import Card from "@/components/Card";

const getAgendaList = async () => {
  const data = await prisma.agenda.findMany({
    select: {
      id: true,
      title: true,
      date: true,
    },
  });
  return data;
};

export default async function AgendaList() {
  const agendaList = await getAgendaList();

  return (
    <div className="p-4 text-[#d8dee9] space-y-4">
      <h1 className="text-xl">Agenda List</h1>
      <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Card agendaList={agendaList} />
      </div>
    </div>
  );
}
