type User = {
  id?: string;
  name: string;
};

type TTestContext = {
  users: User[];
  createUser: (user: User) => void;
};
