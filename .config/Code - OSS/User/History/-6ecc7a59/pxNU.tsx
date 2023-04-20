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
          <Image src={ev.image} alt={"img"} width={300} height={300} />{" "}
        </a>
      ))}
      <a href="/events/london">
        <Image src={"#"} alt={"img"} width={300} height={300} />
        <h2>Events in London</h2>
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam illo
          itaque quisquam fugiat, nobis animi temporibus minima distinctio nihil
          officia, aut delectus amet cum placeat. Distinctio repellat debitis id
          sapiente?
        </p>
      </a>
      <a href="/event/madrid">
        <Image src={"#"} alt={"img"} width={300} height={300} />
        <h2>Events in Madrid</h2>
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam illo
          itaque quisquam fugiat, nobis animi temporibus minima distinctio nihil
          officia, aut delectus amet cum placeat. Distinctio repellat debitis id
          sapiente?
        </p>
      </a>
      <a href="/events/berlin">
        <Image src={"#"} alt={"img"} width={300} height={300} />
        <h2>Events in Berlin</h2>
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam illo
          itaque quisquam fugiat, nobis animi temporibus minima distinctio nihil
          officia, aut delectus amet cum placeat. Distinctio repellat debitis id
          sapiente?
        </p>
      </a>
    </main>
  );
}
