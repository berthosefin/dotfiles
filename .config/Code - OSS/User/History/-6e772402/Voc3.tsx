import Header from "./Header";

export default function Home() {
  return (
    <header className="bg-gray-50">
      <div className="xl:container xl:mx-auto flex flex-col items-center sm:flex-row sm:justify-between text-center py-3">
        <div className="md:flex-none">
          <input type="text" placeholder="Search..." />
        </div>
        <div>
          <a>Design</a>
        </div>
        <div>
          <div className="flex">
            <a>Facebook</a>
            <a>Twitter</a>
            <a>Youtube</a>
          </div>
        </div>
      </div>
    </header>
  );
}
