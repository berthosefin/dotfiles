import Link from "next/link";

export default function Home() {
  return (
    <div className="h-screen w-full homepage">
      <div className="w-4/5 text-center absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
        Explore Tech
        <Link href={"/techGroup"}>Group of Tech</Link>
      </div>
    </div>
  );
}
