import prisma from "@/prisma/client";

const getAgenda = async (id: string) => {
  const data = await prisma.agenda.findUnique({
    where: {
      id,
    },
  });
  return data;
};

type TypeProps = {
  params: {
    id: string;
  };
};

export default async function AgendaDetail({ params }: TypeProps) {
  const agenda = await getAgenda(params.id);

  return (
    <div className="text-slate-100 p-4 md:w-[50vw] lg:w-[30vw]">
      <div key={agenda?.id} className="bg-gray-800 p-4">
        <div className="space-y-2">
          <h1 className="text-2xl">{agenda?.title}</h1>
          <p>{agenda?.date}</p>
          <h3 className="text-lg">Start At: {agenda?.time_start}</h3>
          <h3 className="text-lg">End At: {agenda?.time_end}</h3>
          <h3 className="text-lg">Place: {agenda?.place}</h3>
        </div>
      </div>
    </div>
  );
}
