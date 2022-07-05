using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Controllers
{
    public class AttendanceController : Controller
    {
        private readonly IAttendanceRepository _attendanceRepository;
        private readonly IAnimalRepository _animalRepository;
        private readonly IClinicRepository _clinicRepository;
        private readonly IProcedureRepository _procedureRepository;
        private readonly IVetRepository _vetRepository;
        public AttendanceController(IAnimalRepository animalRepository, IClinicRepository clinicRepository, IProcedureRepository procedureRepository, IVetRepository vetRepository, IAttendanceRepository attendanceRepository)
        {
            _attendanceRepository = attendanceRepository;
            _animalRepository = animalRepository;
            _clinicRepository = clinicRepository;
            _procedureRepository = procedureRepository;
            _vetRepository = vetRepository;
        }

        // GET: Attendance
        public async Task<IActionResult> Index() =>
            View(await _attendanceRepository.GetAll());

        // GET: Attendance/Details/5
        public async Task<IActionResult> Details(int id)
        {
            if (await _attendanceRepository.GetById(id) is Attendance attendance)
                return View(attendance);

            return NotFound();
        }

        // GET: Attendance/Create
        public async Task<IActionResult> Create()
        {
            ViewData["AnimalId"] = new SelectList(await _animalRepository.GetAll(), "Id", "Name");
            ViewData["ClinicId"] = new SelectList(await _clinicRepository.GetAll(), "Id", "Name");
            ViewData["VetId"] = new SelectList(await _vetRepository.GetAll(), "Id", "Name");
            var procedures = await _procedureRepository.GetAll();
            ViewBag.Procedures = procedures;
            ViewData["ProcedureId"] = new MultiSelectList(procedures, "Id", "ProcedureName");
            return View();
        }

        // POST: Attendance/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("AttendanceId,AnimalId,VetId,ClinicId,AttendanceDate,Observation,Procedures")] Attendance attendance, int[] procedures)
        {
            ModelState.Remove(nameof(Attendance.Animal));
            ModelState.Remove(nameof(Attendance.Vet));
            ModelState.Remove(nameof(Attendance.Clinic));
            if (ModelState.IsValid)
            {
                foreach (var procedureId in procedures)
                    if (await _procedureRepository.GetById(procedureId) is Procedure procedure)
                        attendance.Procedures.Add(procedure);

                await _attendanceRepository.Add(attendance);
                return RedirectToAction(nameof(Index));
            }
            ViewData["AnimalId"] = new SelectList(await _animalRepository.GetAll(), "Id", "Name");
            ViewData["ClinicId"] = new SelectList(await _clinicRepository.GetAll(), "Id", "Name");
            ViewData["VetId"] = new SelectList(await _vetRepository.GetAll(), "Id", "Name");
            var proceduresList = await _procedureRepository.GetAll();
            ViewBag.Procedures = proceduresList;
            ViewData["ProcedureId"] = new MultiSelectList(proceduresList, "Id", "ProcedureName");
            return View(attendance);
        }

        // GET: Attendance/Edit/5
        public async Task<IActionResult> Edit(int id)
        {
            if (await _attendanceRepository.GetById(id) is Attendance attendance)
            {
                ViewData["AnimalId"] = new SelectList(await _animalRepository.GetAll(), "Id", "Name");
                ViewData["ClinicId"] = new SelectList(await _clinicRepository.GetAll(), "Id", "Name");
                ViewData["VetId"] = new SelectList(await _vetRepository.GetAll(), "Id", "Name");
                var procedures = await _procedureRepository.GetAll();
                ViewBag.Procedures = procedures;
                ViewData["ProcedureId"] = new MultiSelectList(procedures, "Id", "ProcedureName", attendance.Procedures.Select(p => p.Id).ToArray());
                return View(attendance);
            }
            return NotFound();
        }

        // POST: Attendance/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,AttendanceId,AnimalId,VetId,ClinicId,AttendanceDate,Observation,Procedures")] Attendance attendance, int[] procedures)
        {
            if (id != attendance.Id)
                return NotFound();

            ModelState.Remove(nameof(Attendance.Animal));
            ModelState.Remove(nameof(Attendance.Vet));
            ModelState.Remove(nameof(Attendance.Clinic));

            if (ModelState.IsValid)
            {
                try
                {
                    foreach (var procedureId in procedures)
                    {
                        attendance.Procedures.Clear();
                        if (await _procedureRepository.GetById(procedureId) is Procedure procedure)
                            attendance.Procedures.Add(procedure);
                    }
                    
                    await _attendanceRepository.Update(attendance);
                }
                catch (DbUpdateConcurrencyException)
                {
                    throw;
                }
                return RedirectToAction(nameof(Index));
            }

            ViewData["AnimalId"] = new SelectList(await _animalRepository.GetAll(), "Id", "Name");
            ViewData["ClinicId"] = new SelectList(await _clinicRepository.GetAll(), "Id", "Name");
            ViewData["VetId"] = new SelectList(await _vetRepository.GetAll(), "Id", "Name");
            var proceduresList = await _procedureRepository.GetAll();
            ViewBag.Procedures = proceduresList;
            ViewData["ProcedureId"] = new MultiSelectList(proceduresList, "Id", "ProcedureName", attendance.Procedures.Select(p => p.Id).ToArray());
            return View(attendance);
        }

        // GET: Attendance/Delete/5
        public async Task<IActionResult> Delete(int id)
        {
            if (await _attendanceRepository.GetById(id) is Attendance attendance)
                return View(attendance);

            return NotFound();
        }

        // POST: Attendance/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (await _attendanceRepository.GetById(id) is Attendance attendance)
                await _attendanceRepository.Delete(attendance);

            return RedirectToAction(nameof(Index));
        }
    }
}
