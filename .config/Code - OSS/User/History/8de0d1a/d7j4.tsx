"use client";

import Image from "next/image";
import { useRouter } from "next/navigation";

const Logo = () => {
  const router = useRouter();

  return <Image alt="Logo" className="hidden md:" />;
};

export default Logo;
