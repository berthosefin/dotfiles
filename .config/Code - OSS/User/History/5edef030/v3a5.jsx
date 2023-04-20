import Image from "next/image";
import Link from "next/link";

export default function Section1() {
  return (
    <section className="py-16 ">
      <div className="container mx-auto md:px-20">
        <h1 className="font-bold text-4xl pb-12 text-center">Trending</h1>
        {Slide()}
      </div>
    </section>
  );
}

function Slide() {
  return (
    <div className="grid md:grid-cols-2">
      <div className="Image">
        <Link href={"/"}>
          <Image src={"/images/img1.jpg"} width={300} height={300}></Image>
        </Link>
      </div>
      <div className="Info">
        <div className="cat">
          <Link href={"/"} className="text-orange-600 hover:text-orange-800">
            Business, Travel
          </Link>
          <Link href={"/"} className="text-gray-800 hover:text-gray-600">
            - July 3, 2022
          </Link>
        </div>
        <div className="title">
          <Link
            href={"/"}
            className="text-3xl md:text-6xl font-bold text-gray-800 hover:text-gray-600"
          >
            Lorem ipsum
          </Link>
          <p className="text-gray-500 py-3">
            Sequi aut eius vitae pariatur qui maiores officia, reiciendis
            consequuntur, quia aspernatur a nemo molestiae libero nesciunt nisi
            ducimus obcaecati, doloremque enim.
          </p>
        </div>
      </div>
    </div>
  );
}
