import Image from "next/image";
import Link from "next/link";

export default function Author() {
  return (
    <div className="author flex py-5">
      <Image
        src={"/images/author/author1.jpg"}
        className="rounded-full"
        width={60}
        height={60}
        alt="Author-img"
      />
      <div className="flex flex-col justify-center px-4">
        <Link
          href={"/"}
          className="text-md font-bold text-gray-800 hover:text-gray-600"
        >
          <span className="text-sm text-gray-500">CEO and Fouder</span>
          Thos B
        </Link>
      </div>
    </div>
  );
}
