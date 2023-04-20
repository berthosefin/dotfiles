import Image from "next/image";

export default function Home() {
  return (
    <main>
      <a href="/events/london">
        <Image alt={"img"} width={300} height={300} />
        <h2>Events in London</h2>
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam illo
          itaque quisquam fugiat, nobis animi temporibus minima distinctio nihil
          officia, aut delectus amet cum placeat. Distinctio repellat debitis id
          sapiente?
        </p>
      </a>
      <a href="/event/madrid">
        <Image alt={"img"} width={300} height={300} />
        <h2>Events in Madrid</h2>
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam illo
          itaque quisquam fugiat, nobis animi temporibus minima distinctio nihil
          officia, aut delectus amet cum placeat. Distinctio repellat debitis id
          sapiente?
        </p>
      </a>
      <a href="/events/berlin">
        <Image alt={"img"} width={300} height={300} />
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
