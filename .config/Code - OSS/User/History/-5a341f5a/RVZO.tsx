import { BsFillMoonStarsFill } from "react-icons/bs";
import { AiFillGithub, AiFillLinkedin, AiFillFacebook } from "react-icons/ai";
import Image from "next/image";
import TT from "@/public/TT.png";
import code from "@/public/code.svg";
import development from "@/public/development.svg";
import git from "@/public/git.png";
import php from "@/public/php.png";
import python from "@/public/python.png";

export default function Home() {
  return (
    <main className="bg-[#e5e9f0] px-10 ">
      <section className="min-h-screen">
        <nav className="py-10 mb-12 flex justify-between">
          <h1 className="text-xl font-anurati">THOS TECH</h1>
          <ul className="flex items-center">
            <li>
              <BsFillMoonStarsFill className="cursor-pointer text-2xl" />
            </li>
            <li>
              <a
                className="bg-gradient-to-r from-[#88c0d0] to-[#81a1c1] text-[#e5e9f0] px-4 py-2 rounded-md ml-8"
                href="#"
              >
                Resume
              </a>
            </li>
          </ul>
        </nav>
        <div className="text-center p-10">
          <h2 className="text-5xl py-2 text-[#81a1c1] font-medium">
            Berthose Fin
          </h2>
          <h3 className="text-2xl py-2">Developer Web</h3>
          <p className="text-md py-5 leading-8 text-[#4c566a]">
            Freelance providing serives for programming content needs. Join me
            down below and let`s get cracking!
          </p>
        </div>
        <div className="text-5xl flex justify-center pag-16 py-3 text-[#4c566a]">
          <AiFillGithub />
          <AiFillLinkedin />
          <AiFillFacebook />
        </div>
        <div className="relative mx-auto bg-gradient-to-b from-[#81a1c1] to-[#88c0d0] rounded-full w-80 h-80 mt-5 overflow-hidden">
          <Image src={TT} alt={"TT"} fill />
        </div>
      </section>
      <section>
        <div>
          <h3 className="text-3xl py-1">Services I offer</h3>
          <p className="text-md py-2 leading-8 text-[#4c566a]">
            Sice the beginning of my journey as a freelance developer, I`ve done
            remote work for
            <span className="text-[#88c0d0]"> agencies </span> consulted for{" "}
            <span className="text-[#88c0d0]">startups </span> and collaborated
            with talanted people to create digital products for both business
            and consumer use.
          </p>
          <p className="text-md py-2 leading-8 text-[#4c566a]">
            I offer from a wide range of services, including programming and
            teaching.
          </p>
        </div>
        <div>
          <div className="text-center shadow-lg p-10 rounded-xl my-10">
            <Image src={code} width={100} height={100} alt="design" />
            <h3 className="text-lg font-medium pt-8 pb-2">Lorem</h3>
            <p className="py-2">
              Lorem ipsum dolor, sit amet consectetur adipisicing elit. Labore
              repellat maxime dolores. Consequatur illo, asperiores atque quo
              dolorum similique suscipit amet libero ratione. Quibusdam corporis
              dolores ex dolor obcaecati rem!
            </p>
            <h4 className="py-4 text-[#88c0d0]">Tools I use</h4>
            <p className="text-[#4c566a] py-1">Lorem</p>
            <p className="text-[#4c566a] py-1">Lorem</p>
          </div>
          <div className="text-center shadow-lg p-10 rounded-xl my-10">
            <Image src={development} width={100} height={100} alt="design" />
            <h3 className="text-lg font-medium pt-8 pb-2">Lorem</h3>
            <p className="py-2">
              Lorem ipsum dolor, sit amet consectetur adipisicing elit. Labore
              repellat maxime dolores. Consequatur illo, asperiores atque quo
              dolorum similique suscipit amet libero ratione. Quibusdam corporis
              dolores ex dolor obcaecati rem!
            </p>
            <h4 className="py-4 text-[#88c0d0]">Tools I use</h4>
            <p className="text-[#4c566a] py-1">Lorem</p>
            <p className="text-[#4c566a] py-1">Lorem</p>
          </div>
        </div>
      </section>
      <section>
        <div>
          <h3 className="text-3xl py-1">Portfolio</h3>
          <p className="text-md py-2 leading-8 text-[#4c566a]">
            Sice the beginning of my journey as a freelance developer, I`ve done
            remote work for
            <span className="text-[#88c0d0]"> agencies </span> consulted for{" "}
            <span className="text-[#88c0d0]">startups </span> and collaborated
            with talanted people to create digital products for both business
            and consumer use.
          </p>
          <p className="text-md py-2 leading-8 text-[#4c566a]">
            I offer from a wide range of services, including programming and
            teaching.
          </p>
        </div>
        <div>
          <div>
            <Image src={git} alt="git" />
            <Image src={php} alt="php" />
            <Image src={python} alt="python" />
            <Image src={php} alt="php" />
            <Image src={python} alt="python" />
            <Image src={git} alt="git" />
          </div>
        </div>
      </section>
    </main>
  );
}
