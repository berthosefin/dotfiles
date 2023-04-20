import prisma from "@/prisma/client";

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
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
        {agendaList.map((agenda) => (
          <div className="bg-gray-800 p-4 relative">
            <button className="absolute top-2 right-4">x</button>
            <div className="space-y-2">
              <h1 className="text-2xl">Title</h1>
              <p>Date</p>
            </div>
            <div className="mt-4">
              <button
                className="bg-amber-600 rounded-md hover:bg-amber-700 hover:text-slate-20 px-6 py-2"
                type="submit"
              >
                Add
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
