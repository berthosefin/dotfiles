import Image from "next/image";

export default function Author() {
  return (
    <div className="author flex py-5">
      <Image
        src={"/images/author/author1.jpg"}
        className="rounded-full"
        width={60}
        height={60}
      ></Image>
    </div>
  );
}
