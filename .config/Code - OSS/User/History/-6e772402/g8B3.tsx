import Header from "./Header";

export default function Home() {
  return (
    <header className="bg-gray-50">
      <div className="xl:container xl:mx-auto">
        <div>
          <input type="text" placeholder="Search..." />
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
      </div>
    </header>
  );
}
