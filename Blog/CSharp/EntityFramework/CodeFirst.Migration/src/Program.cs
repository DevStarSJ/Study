using System;
using System.Collections.Generic;
using System.Data.Entity;

namespace EntityFramework_Code_First_Tutorial
{
    class Student
    {
        public int StudentID { get; set; }
        public string StudentName { get; set; }
        public DateTime? DateOfBirth { get; set; }
        public byte[] Photo { get; set; }
        public decimal Height { get; set; }
        public float Weight { get; set; }

        public Standard Standard { get; set; }
        public Teacher Teacher { get; set; }
    }

    class Standard
    {
        public int StandardID { get; set; }
        public string StandardName { get; set; }

        public ICollection<Student> Students { get; set; }
    }

    class Teacher
    {
        public int TeacherID { get; set; }
        public string TeacherName { get; set; }
    }

    class SchoolContext : DbContext
    {
        public DbSet<Student> Students { get; set; }
        public DbSet<Standard> Standards { get; set; }
    }

    class SchoolInitializer : DropCreateDatabaseIfModelChanges<SchoolContext>
    {
        protected override void Seed(SchoolContext context)
        {
            base.Seed(context);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Database.SetInitializer<SchoolContext>(new SchoolInitializer());

            using (var context = new SchoolContext())
            {
                Student s = new Student() { StudentName = "New Student" };

                context.Students.Add(s);
                context.SaveChanges();
            }
        }
    }
}
