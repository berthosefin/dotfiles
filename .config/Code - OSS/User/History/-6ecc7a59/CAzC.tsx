import Image from "next/image";

const importData = async () => {
  const { events_categories } = await import("@/data.json");
  return events_categories;
};

export default async function Home() {
  const data = await importData();

  return (
    <main>
      {data.map((ev) => (
        <a key={ev.id} href={`/events/${ev.id}`}>
          <Image src={"#"} alt={"img"} width={300} height={300} />
          <h2>{ev.title}</h2>
          <p>{ev.description}</p>
        </a>
      ))}
    </main>
  );
}
