using System.ComponentModel.DataAnnotations;

namespace VeterinaryClinic.BL
{
    public class Attendance : IRegistroBancoDados
    {
        public int Id { get; set; }

        public int AnimalId { get; set; }

        [Display(Name = "Animal")]
        public Animal Animal { get; set; }

        public int VetId { get; set; }

        [Display(Name = "Vet")]
        public Vet Vet { get; set; }

        public int ClinicId { get; set; }
        public Clinic Clinic { get; set; }

        [Display(Name = "Procedures")]
        public List<Procedure> Procedures { get; set; }

        public DateTime AttendanceDate { get; set; }

        public string Observation { get; set; }

        public Attendance()
        {
        }

        public Attendance(int id, int animalId, Animal animal, int vetId, Vet vet, int clinicId, Clinic clinic, List<Procedure> procedures, DateTime attendanceDate, string observation)
        {
            Id = id;
            AnimalId = animalId;
            Animal = animal;
            VetId = vetId;
            Vet = vet;
            ClinicId = clinicId;
            Clinic = clinic;
            Procedures = procedures;
            AttendanceDate = attendanceDate;
            Observation = observation;
        }
    }
}